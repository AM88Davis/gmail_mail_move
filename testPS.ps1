$password = ConvertTo-SecureString "GAMers378?!?" -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential ("am88davis@gmail.com", $password)

New-GmailSession -Credential $Cred