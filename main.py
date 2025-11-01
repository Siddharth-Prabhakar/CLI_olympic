#!/usr/bin/env python3
"""
OneLoop Analyzer - Professional Text Processing & Analysis Tool
Author: Siddharth Prabhakar
Constraint: Maximum 1 explicit loop, ≤100 lines total
"""

import re


def clean_text(text: str) -> str:
    """Convert to lowercase, remove punctuation, and normalize whitespace."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def analyze_text(text: str) -> dict:
    """
    Analyze text: count words, get top 5 most common, calculate averages.
    Uses ONE explicit loop for word frequency counting.
    """
    if not text:
        return {'words': 0, 'unique': 0, 'avg_length': 0, 'top_words': []}
    
    words = text.split()
    word_count = {}  # Manual frequency counting in the ONE loop
    total_length = 0
    
    # ONE EXPLICIT LOOP: Count words and their frequencies
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        total_length += len(word)
    
    # Get top 5 words (built-in method, not a loop)
    top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:5]
    
    total_words = len(words)
    unique_count = len(word_count)
    avg_length = total_length / total_words if total_words > 0 else 0
    
    return {
        'words': total_words,
        'unique': unique_count,
        'avg_length': round(avg_length, 1),
        'top_words': top_words
    }


def display_report(data: dict) -> None:
    """Display formatted analysis report with professional formatting."""
    print("\n" + "=" * 50)
    print("           OneLoop Analyzer Report")
    print("=" * 50)
    print(f"Total Words      : {data['words']}")
    print(f"Unique Words     : {data['unique']}")
    print(f"Average Word Length: {data['avg_length']}")
    
    if data['top_words']:
        print("\nMost Common Words:")
        # Use join to avoid loop - print all at once with formatting
        top_str = "\n".join([f"  {word:<15} : {freq}" for word, freq in data['top_words']])
        print(top_str)
    
    print("=" * 50)
    print("Analysis completed successfully.")


def main():
    """Main entry point for the OneLoop Analyzer."""
    print("=" * 50)
    print("         Welcome to OneLoop Analyzer")
    print("=" * 50)
    print("\nEnter your text:")
    
    text_input = input()
    
    if not text_input:
        print("\nNo input provided. Exiting.")
        return
    
    cleaned_text = clean_text(text_input)
    
    if not cleaned_text:
        print("\nNo valid text found after cleaning. Exiting.")
        return
    
    report_data = analyze_text(cleaned_text)
    display_report(report_data)


if __name__ == "__main__":
    main()
