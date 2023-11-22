## Practice with PSCustomObject

$testobj = @([PSCustomObject]@{
    Name = "TONY"
    Age = 35
})

#$testobj += New-Object -TypeName psobject -Property @{Name = "James"; Age = 34}

$testobj | Add-Member -MemberType NoteProperty -name "Country" -Value ""

$testobj += [PSCustomObject]@{
    Name = "Jackson"
    Age = "34"
    Country = "Netherlands"
}

$testobj