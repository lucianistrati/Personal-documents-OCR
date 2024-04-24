# Personal-documents-OCR

# OCR Document Matching and Text Detection

This repository contains a project aimed at performing Optical Character Recognition (OCR) on Romanian baccalaureate diplomas. The project utilizes Hough lines to perform pattern matching between a given document and a standard format of the document. It then applies methods such as Tesseract and Google OCR API to detect text from specific parts of the document, including both the front and back sides.

## Project Overview

The project is organized into several Python scripts:

- `houghLines.py`: Implements the Hough lines algorithm for pattern matching.
- `levenshtein_distance.py`: Provides Levenshtein distance calculation for quality assurance.
- `main.py`: Main script to orchestrate the OCR process.
- `process_back_document.py`: Script for processing the back side of the diploma.
- `process_front_document.py`: Script for processing the front side of the diploma.

## Functionality

1. **Pattern Matching with Hough Lines**: The `houghLines.py` script implements the Hough lines algorithm to perform pattern matching between a given diploma and a standard format of the diploma.

2. **Text Detection with OCR**: The main script `main.py` orchestrates the OCR process. It utilizes methods such as Tesseract and Google OCR API to detect text from specific parts of the diploma.

3. **Quality Assurance with Levenshtein Distance**: The `levenshtein_distance.py` script calculates the Levenshtein distance to ensure the accuracy of OCR outputs, especially in cases of misspelled text.

## Folder Structure

The repository has the following structure:

- `houghLines.py`
- `levenshtein_distance.py`
- `main.py`
- `process_back_document.py`
- `process_front_document.py`

## Usage

1. Clone the repository to your local machine.

2. Ensure you have the required dependencies installed. You may need to install Tesseract OCR and the necessary language packs.

3. Run the appropriate script (`main.py`, `process_back_document.py`, or `process_front_document.py`) to start the OCR process for the respective part of the diploma.

4. Follow the instructions provided by the script to process the diploma and detect text.

## Requirements

The project requires the following dependencies:

- Python 3.x
- OpenCV (for Hough lines algorithm)
- Tesseract OCR
- Google OCR API (optional, if used)
- Levenshtein (for quality assurance)

Install the dependencies using `pip` or any package manager before running the scripts.


[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner2-direct.svg)](https://stand-with-ukraine.pp.ua)
