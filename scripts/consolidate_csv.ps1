$csvPath = "c:\Users\sanjay.waghmare\SOLUTO\docs\SMS_Manual_Test_Cases.csv"
$outPath = "c:\Users\sanjay.waghmare\SOLUTO\docs\SMS_Manual_Test_Cases_Consolidated.csv"
$data = Import-Csv -Path $csvPath -Encoding UTF8
$grouped = $data | Group-Object -Property "Test Case ID"
$outRows = @()
foreach ($g in $grouped) {
    $first = $g.Group[0]
    $stepsAction = ($g.Group | ForEach-Object { "$($_.Step). $($_.Action)" }) -join "`n"
    $stepsResult = ($g.Group | ForEach-Object { "$($_.Step). $($_.'Expected Result')" }) -join "`n"
    $outRows += [PSCustomObject]@{
        "Test Case ID" = $first.'Test Case ID'
        "Title" = $first.Title
        "Scenario" = $first.Scenario
        "Priority" = $first.Priority
        "Step" = ""
        "Action" = $stepsAction
        "Expected Result" = $stepsResult
        "Expected Result (Overall)" = $first.'Expected Result (Overall)'
        "subscriberId" = $first.subscriberId
        "mdn" = $first.mdn
        "serviceEnabled" = $first.serviceEnabled
        "kfsServiceEnabled" = $first.kfsServiceEnabled
        "appleSubscriptionEnabled" = $first.appleSubscriptionEnabled
        "birthday" = $first.birthday
        "gender" = $first.gender
        "brand" = $first.brand
    }
}
$outRows | Export-Csv -Path $outPath -Encoding UTF8 -NoTypeInformation
