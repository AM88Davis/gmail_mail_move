## Practice with PSCustomObject

# Create a PSCustomObject with two Property's (Or Keys)
$testobj = @([PSCustomObject]@{
    Name = "TONY"
    Age = 35
})

#$testobj += New-Object -TypeName psobject -Property @{Name = "James"; Age = 34}

# Adding a Member (Property). This will become a column in a .csv file
$testobj | Add-Member -MemberType NoteProperty -name "Country" -Value ""

#Adding another entry (or a row in a .csv file). Very Useful stuff
$testobj += [PSCustomObject]@{
    Name = "Jackson"
    Age = "34"
    Country = "Netherlands"
}

# This will print the results. Just for testing purposes.
$testobj

# Exports to CSV file and DOES Append
$testobj | Export-Csv -Path c:\users\anthony.davis\pycharmprojects\gmail_project1\testpsobjectps1.csv -Append 

# Exports to CSV file and DOES NOT Append. Rewrites the existing file
$testobj | Export-Csv -Path c:\users\anthony.davis\pycharmprojects\gmail_project1\testpsobjectps1.csv


