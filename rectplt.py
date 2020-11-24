import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image

# Display the image
plt.imshow(Image.open('page3.png'))

# Add the patch to the Axes
plt.gca().add_patch(Rectangle((50,100),40,30,linewidth=1,edgecolor='r',facecolor='none'))
plt.show()