# Yasna 31: TEI P5 Digital Edition & Extraction Pipeline

This repository demonstrates the digital transformation of philological research data from my PhD dissertation (*Yasna 31: An Analysis of the Avestan, Zand and Sanskrit Versions*, University of Tehran, 2016) into a machine-readable format.

## 🎯 Project Goals
The objective of this project is to model complex multilingual Zoroastrian texts according to modern **FAIR data principles**, specifically designed for integration into the **CRC 1475 "Metaphors of Religion"** infrastructure.

## 🛠️ Technical Implementation
- **TEI P5 Encoding**: Structured XML modeling of Avestan stanzas, Persian translations, and Sanskrit parallels.
- **Multilingual Modeling**: Handling Avestan (Latin-script diacritics), Sanskrit, and RTL Persian scripts within a single UTF-8 encoded source.
- **Python Data Pipeline**: An automated extraction script (`parse-yasna.py`) designed to retrieve linguistic data for database ingestion and comparative analysis.

## 📂 Repository Structure
- `Yasna31_Edition.xml`: The primary TEI P5 source file.
- `parse-yasna.py`: Python script utilizing `xml.etree.ElementTree` for data extraction.
- `new_env/`: (Local) Python virtual environment for dependency management.

## 🚀 How to Run
1. Activate the environment: `.\new_env\Scripts\Activate.ps1`
2. Run the parser: `python parse-yasna.py`
