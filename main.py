import sys
from qa_system import answer_question

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <pdf_file_path> <question>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    question = sys.argv[2]

    answer = answer_question(pdf_path, question)
    print("Answer:", answer)

if __name__ == "__main__":
    main()