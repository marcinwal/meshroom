import sys
from meshroom.core import desc


class StructureFromMotion(desc.CommandLineNode):
    internalFolder = '{cache}/{nodeType}/{uid0}/'
    commandLine = 'aliceVision_incrementalSfM {allParams} --allowUserInteraction 0'
    size = desc.DynamicNodeSize('input')

    inputs = [
        desc.File(
            name='input',
            label='Input',
            description='''SfMData file.''',
            value='',
            uid=[0],
        ),

        desc.File(
            name='featuresFolder',
            label='Features Folder',
            description='''Path to a folder containing the extracted features.''',
            value='',
            uid=[0],
        ),
        desc.File(
            name='matchesFolder',
            label='Matches Folder',
            description='''Path to a folder in which computed matches are stored.''',
            value='',
            uid=[0],
        ),
        desc.ChoiceParam(
            name='describerTypes',
            label='Describer Types',
            description='''Describer types used to describe an image.''',
            value=['SIFT'],
            values=['SIFT', 'SIFT_FLOAT', 'AKAZE', 'AKAZE_LIOP', 'AKAZE_MLDB', 'CCTAG3', 'CCTAG4', 'SIFT_OCV',
                    'AKAZE_OCV'],
            exclusive=False,
            uid=[0],
            joinChar=',',
        ),
        desc.ChoiceParam(
            name='interFileExtension',
            label='Inter File Extension',
            description='''Extension of the intermediate file export.''',
            value='.abc',
            values=('.abc', '.ply'),
            exclusive=True,
            uid=[],
        ),
        desc.BoolParam(
            name='useLocalBA',
            label='Local Bundle Adjustment',
            description='It reduces the reconstruction time, especially for large datasets (500+ images),\n'
                        'by avoiding computation of the Bundle Adjustment on areas that are not changing.',
            value=False,
            uid=[0],
        ),
        desc.IntParam(
            name='minInputTrackLength',
            label='Min Input Track Length',
            description='''Minimum track length in input of SfM''',
            value=2,
            range=(2, 10, 1),
            uid=[0],
        ),
        desc.IntParam(
            name='maxNumberOfMatches',
            label='Maximum Number of Matches',
            description='Maximum number of matches per image pair (and per feature type). \n'
                        'This can be useful to have a quick reconstruction overview. \n'
                        '0 means no limit.',
            value=0,
            range=(0, 50000, 1),
            uid=[0],
        ),
        desc.ChoiceParam(
            name='cameraModel',
            label='Camera Model',
            description="1: Pinhole \n"
                        "2: Pinhole 2\n"
                        "3: Pinhole 3",
            value=3,
            values=[1, 2, 3],
            exclusive=True,
            uid=[0],
        ),
        desc.File(
            name='initialPairA',
            label='Initial Pair A',
            description='''Filename of the first image (without path).''',
            value='',
            uid=[0],
        ),
        desc.File(
            name='initialPairB',
            label='Initial Pair B',
            description='''Filename of the second image (without path).''',
            value='',
            uid=[0],
        ),
        desc.ChoiceParam(
            name='verboseLevel',
            label='Verbose Level',
            description='''Verbosity level (fatal, error, warning, info, debug, trace).''',
            value='info',
            values=['fatal', 'error', 'warning', 'info', 'debug', 'trace'],
            exclusive=True,
            uid=[],
        )
    ]

    outputs = [
        desc.File(
            name='output',
            label='Output SfM data file',
            description='''Path to the output sfmdata file''',
            value='{cache}/{nodeType}/{uid0}/sfm.abc',
            uid=[],
        ),
        desc.File(
            name='extraInfoFolder',
            label='Output',
            description='''Folder for intermediate reconstruction files and additional reconstruction information files.''',
            value='{cache}/{nodeType}/{uid0}/',
            uid=[],
        ),
    ]
