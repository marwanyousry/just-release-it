from xml.dom import minidom


def update_exported_attribute(xml_file_path):
    # Parse the XML file
    doc = minidom.parse(xml_file_path)

    # Find the receiver with intent-filter
    receivers = doc.getElementsByTagName("receiver")
    for receiver in receivers:
        intent_filters = receiver.getElementsByTagName("intent-filter")
        if intent_filters:
            # Check if exported attribute is not already set
            if not receiver.hasAttribute('android:exported'):
                # Add android:exported="true" attribute
                receiver.setAttribute('android:exported', 'true')

    # Save the modified XML file
    with open(xml_file_path, 'w', encoding='utf-8') as f:
        doc.writexml(f, indent='', newl='', encoding='utf-8')

if __name__ == "__main__":
    xml_file_path = "./../../android/capacitor-cordova-android-plugins/src/main/AndroidManifest.xml"
    update_exported_attribute(xml_file_path)


