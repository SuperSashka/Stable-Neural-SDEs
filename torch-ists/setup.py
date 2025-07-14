from setuptools import setup, find_packages

install_requires = [
    'ray',
    'numpy',
    'pandas',
    'matplotlib',
    'scipy',
    'scikit-learn',
    'tqdm',
    'sktime',
    'stribor',
    'torchcde',
    'torchdiffeq',
    'torchdyn',
    'torchmetrics',
    'torchsde',
]

# with open('README.md', 'r') as f:
#     long_description = f.read()

setup(name='torch_ists',
      version='0.5.0',
      description='Pytorch ISTS',
      # long_description=long_description,
      # long_description_content_type='text/markdown',
      url='',
      author='',
      author_email='',
      packages=find_packages(),
      install_requires=install_requires,
      python_requires='>=3.9',
      zip_safe=False,
)