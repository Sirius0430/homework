from osgeo import gdal
import os

def get_dataset_band(bandfile):
    input_dataset = gdal.Open(bandfile)
    input_band = input_dataset.GetRasterBand(1)
    return [input_dataset, input_band]


def main():
    os.chdir(r'D:\行政\武大\课程\Signal Processing')
    bandfile_1 = 'LC08_L1TP_123039_20130613_20170504_01_T1_B4.TIF'
    bandfile_2 = 'LC08_L1TP_123039_20130613_20170504_01_T1_B3.TIF'
    bandfile_3 = 'LC08_L1TP_123039_20130613_20170504_01_T1_B2.TIF'
    bandfile = [bandfile_1, bandfile_2, bandfile_3]

    inputdata = []
    for i in range(3):
        inputdata.append(get_dataset_band(bandfile[i]))
    inputdataset_1, inputband_1 = inputdata[0]

    file_driver = gdal.GetDriverByName('Gtiff')
    output_dataset = file_driver.Create(
        'data.tif', inputband_1.XSize, inputband_1.YSize, 3, inputband_1.DataType
    )
    output_dataset.SetProjection(inputdataset_1.GetProjection())
    output_dataset.SetGeoTransform(inputdataset_1.GetGeoTransform())

    for i in range(3):
        inputband_data = inputdata[i][1].ReadAsArray()
        output_dataset.GetRasterBand(i + 1).WriteArray(inputband_data)

    output_dataset.BuildOverviews('average', [2, 4, 8, 16, 32])

if __name__ == '__main__':
    main()