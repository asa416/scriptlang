from distutils.core import setup

setup(
    name='TicTacToe',
    version='1.0',

    py_modules=['Tic-Tac-Toe'],

    packages=['images'],
    package_data={'images':['*.gif']},
)