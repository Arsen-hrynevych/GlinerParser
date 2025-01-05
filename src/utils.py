import json
import re
import os

import pdfplumber

from config import model, RESUME_ENTITY_TYPES


def extract_resume_entities(
    resume_text: str, confidence_threshold: float = 0.5
) -> dict:
    """
    Extract structured information from resume text using named entity recognition.

    Args:
        resume_text (str): The plain text content of the resume
        confidence_threshold (float): Minimum confidence score for entity extraction

    Returns:
        dict: Dictionary mapping entity types to lists of extracted text
              e.g. {"Skills": ["Python", "Java"], "Education": ["BS Computer Science"]}
    """
    detected_entities = model.predict_entities(
        resume_text, RESUME_ENTITY_TYPES, threshold=confidence_threshold
    )

    structured_entities = {}

    for entity in detected_entities:
        entity_type = entity["label"]
        entity_text = entity["text"]
        structured_entities.setdefault(entity_type, []).append(entity_text)

    return structured_entities


def read_resume_file(resume_file_path: str) -> str:
    """
    Read resume file content as text.

    Args:
        resume_filepath (str): Path to the resume file

    Returns:
        str: Raw text content of the resume

    Raises:
        FileNotFoundError: If resume file doesn't exist
        UnicodeDecodeError: If file encoding is not UTF-8
    """
    if not resume_file_path.lower().endswith(".pdf"):
        raise ValueError(f"File must be a PDF: {resume_file_path}")

    try:
        with pdfplumber.open(resume_file_path) as pdf:
            text_content = ""
            for page in pdf.pages:
                text_content += page.extract_text() + "\n"

            # Clean the extracted text
            cleaned_content = clean_text(text_content)
            return cleaned_content
    except Exception as exc:
        raise Exception(f"Error extract data from PDF file: {str(exc)}")


def save_results_to_json(extracted_entities: dict, json_output_path: str) -> None:
    """
    Save extracted resume entities to a JSON file.

    Args:
        extracted_entities (dict): Dictionary of entities extracted from the resume
        json_output_path (str): Destination path for the JSON output file

    Raises:
        PermissionError: If writing to output path is not allowed
        OSError: If output directory doesn't exist
    """
    resume_data = []
    if os.path.exists(json_output_path):
        with open(json_output_path, "r", encoding="utf-8") as json_file:
            resume_data = json.load(json_file) if os.path.getsize(json_output_path) > 0 else []
            resume_data = [resume_data] if isinstance(resume_data, dict) else resume_data

    resume_data.append(extracted_entities)
    with open(json_output_path, "w", encoding="utf-8") as parsed_resume:
        json.dump(resume_data, parsed_resume, ensure_ascii=False, indent=4)


def clean_text(raw_text: str) -> str:
    """
    Clean and Remove non-ASCII characters and problematic symbols.

    Args:
        raw_text (str): Raw text content

    Returns:
        str: Cleaned and normalized text
    """
    cleaned_text = re.sub(r"[^\x00-\x7F]+", " ", raw_text)
    cleaned_text = re.sub(r"[\`^\\x(cid:17)]", "", raw_text)
    cleaned_text = re.sub(r"\s+", " ", raw_text).strip()
    return cleaned_text
