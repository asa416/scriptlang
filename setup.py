from distutils.core import setup, Extension

module_rect = Extension('rect', sources=['rectmodule.cpp'])

setup(
    name='PublicFacility',
    version='1.0',

    py_modules=['data', 'image', 'main', 'mapview', 'send_email'],

    packages=['images'],
    package_data={'images':['*.png']},

    ext_modules=[module_rect],
)