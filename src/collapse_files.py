#!/usr/bin/env python3
"""
Script to collapse all files in a directory into a single printable output.
Each file's content is prefixed with its path for easy identification.
"""

import os
import sys
from pathlib import Path


def should_skip(path, skip_patterns=None):
    """Check if a file or directory should be skipped."""
    if skip_patterns is None:
        skip_patterns = {
            '__pycache__', '.git', '.svn', '.hg', 'node_modules',
            '.venv', 'venv', 'env', '.env', '.idea', '.vscode',
            '*.pyc', '*.pyo', '*.so', '*.dylib', '*.dll'
        }
    
    name = path.name
    
    # Skip hidden files/folders
    if name.startswith('.') and name not in {'.gitignore', '.env.example'}:
        return True
    
    # Skip common directories and patterns
    if name in skip_patterns:
        return True
    
    # Skip binary-like extensions
    binary_exts = {'.pyc', '.pyo', '.so', '.dylib', '.dll', '.exe', 
                   '.jpg', '.jpeg', '.png', '.gif', '.pdf', '.zip', 
                   '.tar', '.gz', '.bz2', '.db', '.sqlite'}
    if path.suffix.lower() in binary_exts:
        return True
    
    return False


def is_text_file(file_path, max_check_bytes=8192):
    """Check if a file is likely a text file."""
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(max_check_bytes)
            if b'\x00' in chunk:  # Null bytes suggest binary
                return False
        return True
    except:
        return False


def collapse_files(directory='.', output_file=None):
    """
    Collapse all files in directory into a single output.
    
    Args:
        directory: Root directory to scan (default: current directory)
        output_file: Optional file path to write output (default: print to stdout)
    """
    root_path = Path(directory).resolve()
    
    if not root_path.exists():
        print(f"Error: Directory '{directory}' does not exist.", file=sys.stderr)
        return
    
    output_lines = []
    output_lines.append("=" * 80)
    output_lines.append(f"COLLAPSED FILES FROM: {root_path}")
    output_lines.append("=" * 80)
    output_lines.append("")
    
    # Collect all files
    files_processed = 0
    files_skipped = 0
    
    for file_path in sorted(root_path.rglob('*')):
        if file_path.is_file():
            # Check if should skip
            if should_skip(file_path):
                files_skipped += 1
                continue
            
            # Check if text file
            if not is_text_file(file_path):
                files_skipped += 1
                continue
            
            # Get relative path for cleaner output
            try:
                relative_path = file_path.relative_to(root_path)
            except ValueError:
                relative_path = file_path
            
            # Add file header
            output_lines.append("-" * 80)
            output_lines.append(f"FILE: {relative_path}")
            output_lines.append("-" * 80)
            
            # Read and add file content
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    output_lines.append(content)
                    if not content.endswith('\n'):
                        output_lines.append('')
                files_processed += 1
            except Exception as e:
                output_lines.append(f"[ERROR reading file: {e}]")
                output_lines.append('')
                files_skipped += 1
            
            output_lines.append('')
    
    # Add summary
    output_lines.append("=" * 80)
    output_lines.append(f"SUMMARY: {files_processed} files processed, {files_skipped} files skipped")
    output_lines.append("=" * 80)
    
    # Output results
    result = '\n'.join(output_lines)
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"Output written to: {output_file}")
    else:
        print(result)


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Collapse all files in a directory into a single output for easy copying.'
    )
    parser.add_argument(
        'directory',
        nargs='?',
        default='.',
        help='Directory to process (default: current directory)'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output file path (default: print to stdout)'
    )
    
    args = parser.parse_args()
    
    collapse_files(args.directory, args.output)