from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 

def get_approx_matrix(u, sigma, v, rank): #rank indicates the number of reserved singular values ​​of truncated SVD
    m = len(u)
    n = len(v)
    a = np.zeros((m, n))
    k = 0
    while k < rank:
        uk = u[:, k].reshape(m, 1)
        vk = v[k].reshape(1, n)
        a += sigma[k] * np.dot(uk, vk)
        k += 1
    a[a < 0] = 0
    a[a > 255] = 255
    return a.astype("uint8")

def get_svd_image(file_path):
    name, suffix = file_path.split(".")
    img = Image.open(file_path, 'r')
    a = np.array(img)
    u0, sigma0, v0 = np.linalg.svd(a[:, :, 0])
    u1, sigma1, v1 = np.linalg.svd(a[:, :, 1])
    u2, sigma2, v2 = np.linalg.svd(a[:, :, 2])
    print("origin image \n red rank:",len(sigma0), " green_rank:", 
          len(sigma1)," blue_rank:", len(sigma2))
    for rank in np.arange(50, 500, 50):
        red_matrix = get_approx_matrix(u0, sigma0, v0, rank)
        green_matrix = get_approx_matrix(u1, sigma1, v1, rank)
        blue_matrix = get_approx_matrix(u2, sigma2, v2, rank)
        I = np.stack((red_matrix, green_matrix, blue_matrix), 2)
        Image.fromarray(I).save(name + str(rank) + "." +suffix)    


get_svd_image("wbb.jpg")
plt.figure(figsize=(40.32,26.88))
for i in range(1, 10, 1):
    ax = plt.subplot(3,3,i)
    img = mpimg.imread("wbb" + str(i*50) + ".jpg") 
    ax.imshow(img)
    ax.set_title("rank:"+str(i*50))
    ax.set_axis_off()
plt.savefig('wbb_svd_compare.png')
plt.show()

