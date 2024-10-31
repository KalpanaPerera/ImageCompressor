from PIL import Image as I
import os
import glob
k=1

def compress_images(input_folder, output_folder):
    # Ensure output folder exists
    z=0
    os.makedirs(output_folder, exist_ok=True)

    # Get all image files in the input folder
    image_files = glob.glob(os.path.join(input_folder, '*.jpg'))

    for img in image_files:
        # Open image
        px = I.open(img)
        xx, yy = px.size
        emtliney = 0
        emtlinex = 0
        emtly = []
        emtlx = []

        print(f"Processing {img} ({xx}x{yy})")

        # Find non-empty rows
        for y in range(yy):
            for x in range(xx):
                co = x, y
                a, *b = px.getpixel(co)
                if a < 150 :
                    emtly.append(y)
                    z=1
                    break
                elif z==1:
                    z=0
                    emtliney -= 1
                    emtly.append(y)

            else:
                emtliney += 1

        # Find non-empty columns
        for x in range(xx):
            for y in range(yy):
                co = x, y
                a, *b = px.getpixel(co)
                if a < 100:
                    emtlx.append(x)
                    break
            else:
                emtlinex += 1

        # Calculate new image size
        y2 = yy - emtliney
        x2 = xx - emtlinex
        im = I.new("RGB", (x2, y2))
        pix = im.load()
        l = 0

        # Copy non-empty pixels to new image
        for y in range(y2):
            line = emtly[l]
            x = 0
            for ex in emtlx:
                co = ex, line
                c = px.getpixel(co)
                pix[x, y] = c
                x += 1
            l += 1

        # Save compressed image to output folder
        img_name = os.path.basename(img)
        imgout = os.path.splitext(img_name)[0] + ' (compressed).jpg'
        output_path = os.path.join(output_folder, imgout)
        im.save(output_path, 'JPEG')

        print(f"Saved compressed image as {output_path}")


# Input and output folder paths
input_folder = input('Enter the path to the folder containing images: ')
#output_folder = input('Enter the path to the folder for saving compressed images: ')
input_folder=input_folder.replace('"','')
output_folder=input_folder+' (Compressed)'
compress_images(input_folder, output_folder)from PIL import Image as I
import os
import glob
k=1

def compress_images(input_folder, output_folder):
    # Ensure output folder exists
    z=0
    os.makedirs(output_folder, exist_ok=True)

    # Get all image files in the input folder
    image_files = glob.glob(os.path.join(input_folder, '*.jpg'))

    for img in image_files:
        # Open image
        px = I.open(img)
        xx, yy = px.size
        emtliney = 0
        emtlinex = 0
        emtly = []
        emtlx = []

        print(f"Processing {img} ({xx}x{yy})")

        # Find non-empty rows
        for y in range(yy):
            for x in range(xx):
                co = x, y
                a, *b = px.getpixel(co)
                if a < 150 :
                    emtly.append(y)
                    z=1
                    break
                elif z==1:
                    z=0
                    emtliney -= 1
                    emtly.append(y)

            else:
                emtliney += 1

        # Find non-empty columns
        for x in range(xx):
            for y in range(yy):
                co = x, y
                a, *b = px.getpixel(co)
                if a < 100:
                    emtlx.append(x)
                    break
            else:
                emtlinex += 1

        # Calculate new image size
        y2 = yy - emtliney
        x2 = xx - emtlinex
        im = I.new("RGB", (x2, y2))
        pix = im.load()
        l = 0

        # Copy non-empty pixels to new image
        for y in range(y2):
            line = emtly[l]
            x = 0
            for ex in emtlx:
                co = ex, line
                c = px.getpixel(co)
                pix[x, y] = c
                x += 1
            l += 1

        # Save compressed image to output folder
        img_name = os.path.basename(img)
        imgout = os.path.splitext(img_name)[0] + ' (compressed).jpg'
        output_path = os.path.join(output_folder, imgout)
        im.save(output_path, 'JPEG')

        print(f"Saved compressed image as {output_path}")


# Input and output folder paths
input_folder = input('Enter the path to the folder containing images: ')
#output_folder = input('Enter the path to the folder for saving compressed images: ')
input_folder=input_folder.replace('"','')
output_folder=input_folder+' (Compressed)'
compress_images(input_folder, )