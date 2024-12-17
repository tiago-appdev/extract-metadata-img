from PIL import Image, ExifTags
import sys
import os

def clear_screen():
    # Clear the screen on Windows and Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def get_exif(filename):
    exif_data = {}
    image = Image.open(filename)
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = ExifTags.TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for gps_tag in value:
                    sub_decoded = ExifTags.GPSTAGS.get(gps_tag, gps_tag)
                    gps_data[sub_decoded] = value[gps_tag]
                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value
    return exif_data

def gps_extract(exif_dict):
    if 'GPSInfo' not in exif_dict:
        return "No GPS metadata found."
    
    gps_metadata = exif_dict['GPSInfo']
    lat_ref_num = 1 if gps_metadata['GPSLatitudeRef'] == 'N' else -1
    long_ref_num = 1 if gps_metadata['GPSLongitudeRef'] == 'E' else -1

    lat_list = [float(num) for num in gps_metadata['GPSLatitude']]
    long_list = [float(num) for num in gps_metadata['GPSLongitude']]

    lat_coordinate = (lat_list[0] + lat_list[1]/60 + lat_list[2]/3600) * lat_ref_num
    long_coordinate = (long_list[0] + long_list[1]/60 + long_list[2]/3600) * long_ref_num

    return (lat_coordinate, long_coordinate)

def no_meta(filename):
    # Open the image
    img = Image.open(filename)
    # Get the file extension
    ext = os.path.splitext(filename)[1]  # Return (name, extension)
    output_file = f"no_meta{ext}"  # Create a new file name
    # Save the image without metadata
    img.save(output_file)
    print(f"Image saved without metadata as '{output_file}'.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_metadata.py <image_path>")
        return

    image = sys.argv[1]

    while True:
        print("\nMenu:")
        print("1. Extract metadata from image")
        print("2. Extract coordinates GPS from image")
        print("3. Remove metadata from image")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            clear_screen()
            exif_data = get_exif(image)
            print("\nMetadata:")
            for key, value in exif_data.items():
                print(f"{key}: {value}")
        elif choice == '2':
            clear_screen()
            exif_data = get_exif(image)
            gps = gps_extract(exif_data)
            print("\nCoordinates GPS:")
            print(gps)
        elif choice == '3':
            clear_screen()
            no_meta(image)
        elif choice == '4':
            clear_screen()
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
