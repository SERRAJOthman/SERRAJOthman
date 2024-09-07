
You can use the Python `matplotlib` library to display the images. Here is a simple code snippet that allows you to choose which image to display by typing "1" or "2":

```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def display_image(choice):
    if choice == "1":
        img_path = 'Screenshot_20240907-141421_ChatGPT.jpg'  # Replace with the actual path to your first image
    elif choice == "2":
        img_path = 'path_to_image_2.png'  # Replace with the actual path to your second image
    else:
        print("Invalid choice. Please enter '1' or '2'.")
        return

    img = mpimg.imread(img_path)
    plt.imshow(img)
    plt.axis('off')  # Hide axes
    plt.show()

# Ask the user for their choice
choice = input("Enter '1' to display the first image or '2' to display the second image: ")
display_image(choice)
```

Make sure to replace `'path_to_image_1.png'` and `'path_to_image_2.png'` with the actual paths to your images.
