# st =  """
# $gen write a letter to principal for leave for 3 days because of my big brother marriage.
# $gen write a letter 
# lorem porem jfkdjshfiuds hfdkhlsk uheilkhfd. hjfidksld 
# """

# aicmd =["$gen","$ai"] 

# startindex = st.find(aicmd)
# endI = st.find('.')

# extractext = st[startindex+len(x if x in aicmd):endI].strip()
# print(extractext)

# Your input string
st = """
$ai write a letter to principal for leave for 3 days because of my big brother marriage.

lorem porem jfkdjshfiuds hfdkhlsk uheilkhfd. hjfidksld
"""

# List of commands to look for
aicmd = ["$gen", "$ai"]

# Initialize variables
start_index = None
end_index = None

# Find the first occurrence of any command in the string
for cmd in aicmd:
    if cmd in st:
        start_index = st.find(cmd)
        break

# Find the index of the first period (".") after the command
if start_index is not None:
    end_index = st.find(".", start_index)

# Extract the desired substring
if start_index is not None and end_index != -1:
    extracted_line = st[start_index + len(cmd):end_index].strip()
    print(extracted_line)
else:
    print("No relevant line found.")

# Note: This assumes there is only one occurrence of the specified command.
# If there are multiple occurrences, additional logic may be needed.
