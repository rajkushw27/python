# commands to upload to the pypi test repository

# Create sdist and bdist First
# python3 setup.py sdist bdist_wheel

# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# pip install --index-url https://test.pypi.org/simple/ rajkushw

# command to upload to the pypi repository
# twine upload dist/*
# pip install rajkushw


from rajkushw import Total_sum
print(Total_sum.sumOfNumbers(1, 2, 3))
