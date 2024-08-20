from xml.dom import minidom

def remove_param_onload(xml_file_path):
    # Parse the XML file
    doc = minidom.parse(xml_file_path)

    # Find all elements with the specified parent and attribute values
    feature_elements = doc.getElementsByTagName('feature')
    for feature_element in feature_elements:
        if feature_element.getAttribute('name') == 'LottieSplashScreen':
            param_elements = feature_element.getElementsByTagName('param')
            for param_element in param_elements:
                if param_element.getAttribute('name') == 'onload' and param_element.getAttribute('value') == 'true':
                    # Remove the param element
                    feature_element.removeChild(param_element)

    # Save the modified XML back to the file with the original encoding
    with open(xml_file_path, 'wb') as file:
        file.write(doc.toxml(encoding='utf-8'))

# Example usage
xml_file_path = './../../ios/App/App/config.xml'
remove_param_onload(xml_file_path)