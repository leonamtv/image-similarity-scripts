from core.mse import mse
from core.rmse import rmse
from core.psnr import psnr
from core.uqi import uqi
from core.ssim import ssim
from core.ergas import ergas
from core.scc import scc
from core.rase import rase
from core.sam import sam
from core.msssim import msssim
from core.vifp import vifp

test_image_1 = './test_images/test_image_1.JPG'
test_image_2 = './test_images/test_image_2.JPG'

print('mse=' + str(mse(test_image_1, test_image_2)))
print('rmse=' + str(rmse(test_image_1, test_image_2)))
print('psnr=' + str(psnr(test_image_1, test_image_2)))
print('uqi=' + str(uqi(test_image_1, test_image_2)))
print('ssim=' + str(ssim(test_image_1, test_image_2)))
print('ergas=' + str(ergas(test_image_1, test_image_2)))
print('scc=' + str(scc(test_image_1, test_image_2)))
print('rase=' + str(rase(test_image_1, test_image_2)))
print('sam=' + str(sam(test_image_1, test_image_2)))
print('msssim=' + str(msssim(test_image_1, test_image_2)))
print('vifp=' + str(vifp(test_image_1, test_image_2)))