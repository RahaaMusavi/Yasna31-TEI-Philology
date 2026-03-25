import xml.etree.ElementTree as ET

def parse_yasna_data(xml_file):
    # TEI files use a specific namespace. We must define it to find the tags.
    ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
    
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        print("="*60)
        print("YASNA 31.1 - LINGUISTIC DATA EXTRACTION")
        print("="*60)

        # 1. Extract the primary Avestan text
        for stanza in root.findall('.//tei:div[@type="stanza"]', ns):
            stanza_no = stanza.get('n')
            print(f"\n[Stanza {stanza_no}]")
            
            avestan_lines = stanza.findall('.//tei:cit[@type="venerable-avestan"]/tei:l', ns)
            for line in avestan_lines:
                print(f"Avestan: {line.text}")

            # 2. Extract the Persian translation
            persian_text = stanza.find('.//tei:div[@type="translation"]/tei:p', ns)
            if persian_text is not None:
                print(f"Persian Translation: {persian_text.text}")

            # 3. Extract the philological analysis
            print("\n--- Philological Analysis ---")
            for entry in stanza.findall('.//tei:entry', ns):
                lemma_node = entry.find('tei:form/tei:lemma', ns)
                if lemma_node is not None:
                    lemma = lemma_node.text
                    sanskrit = entry.find('.//tei:mentioned[@xml:lang="sa"]', ns)
                    sanskrit_val = sanskrit.text if sanskrit is not None else "N/A"
                    print(f"Word: {lemma:<15} | Sanskrit Parallel: {sanskrit_val}")
    except FileNotFoundError:
        print(f"Error: The file '{xml_file}' was not found. Make sure it is in the same folder.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # This must match the exact name of your XML file
    parse_yasna_data('Yasna31_Edition.xml')