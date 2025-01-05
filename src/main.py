from os import environ, path, listdir
from pathlib import Path

from dotenv import load_dotenv

from utils import read_resume_file, save_results_to_json, extract_resume_entities


ROOT_PATH = Path(__file__).parent.parent / ".env"

load_dotenv()


def process_resume(resume_path: str, output_path: str) -> None:
    """
    Process a single resume file and save the extracted information.

    Args:
        resume_path (str): Path to the input resume file
        output_path (str): Path where the parsed JSON will be saved
    """
    try:
        resume_content = read_resume_file(resume_path)

        structured_resume_data = extract_resume_entities(resume_content, 0.3)

        structured_resume_data["source_file"] = path.basename(resume_path)

        save_results_to_json(structured_resume_data, output_path)

        print(f"Successfully processed: {resume_path}")
    except Exception as exc:
        print(f"Error processing {resume_path}: {str(exc)}")


def process_resumes():
    """
    Process all resume files in the specified directory.

    Environment Variables Required:
        RESUMES_FILE_PATH: Path to the directory containing resume files
        PARSED_RESUMES_FILE_PATH: Path where the parsed JSON will be saved

    Flow:
        1. Scans the input directory for PDF files
        2. Processes each PDF file:
            - Reads resume content
            - Extracts entities using GLiNER model
            - Saves structured data as JSON
        3. Combines all results into a single JSON file

    Raises:
        KeyError: If required environment variables are not set
        FileNotFoundError: If input directory doesn't exist
        PermissionError: If unable to write to output path
    """
    resumes_dir = environ["RESUMES_FILE_PATH"]
    parsed_resumes_path = environ["PARSED_RESUMES_FILE_PATH"]

    # Process all PDF files in the directory
    pdf_files = [f for f in listdir(resumes_dir) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print(f"No PDF files found in {resumes_dir}")
        return

    for pdf_file in pdf_files:
        resume_path = path.join(resumes_dir, pdf_file)
        process_resume(resume_path, parsed_resumes_path)

    print(f"Processing complete. Results saved to {parsed_resumes_path}")


if __name__ == "__main__":
    process_resumes()
