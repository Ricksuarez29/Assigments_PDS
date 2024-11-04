# README - Session 5 PDS

## Exercise
Reusing the same annotations we worked with in the previous session, we answer the some exercises with new libraries.

## Libraries Used
- **os**: To navigate and manipulate file paths.
- **glob**: For pattern matching file paths.
- **re**: For using regular expressions to match the naming convention.
- **datetime**: To handle and manipulate date and time information.
- **pandas**: To create and manipulate dataframes for analysis.
- **json**: For saving and loading data in JSON format.
- **pickle**: For serializing and deserializing Python objects.

## Brief Explanation

### Step-by-Step Guide:

1. **Annotations per Month and Year**:
    - Extract dates from the filenames using `datetime.strptime()` and organize them using `pandas` to count and identify the month with the most annotation files.

2. **Dictionary Creation**:
    - Create a dictionary with months as keys and a list of annotation names as values. Save this dictionary in both JSON and Pickle formats.

3. **Sort Annotations**:
    - Filter annotations for the second half of 2024, create a DataFrame to store them, and sort them by date using `pandas`.