<?php
$conversionResult = null;

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['amount'], $_POST['from_currency'], $_POST['to_currency'])) {
    $amount = $_POST['amount'];
    $from_currency = $_POST['from_currency'];
    $to_currency = $_POST['to_currency'];
    
    // API key and URL for ExchangeRate API
    $apiKey = "YOUR_API_KEY_HERE";  // Replace with your API key
    $url = "https://v6.exchangerate-api.com/v6/$apiKey/latest/$from_currency";
    
    // Get the JSON response from the API
    $jsonResponse = file_get_contents($url);
    $exchangeData = json_decode($jsonResponse, true);
    
    if ($exchangeData['result'] === 'success') {
        // Get exchange rate for the desired currency
        $exchangeRate = $exchangeData['conversion_rates'][$to_currency];
        
        // Calculate the converted amount
        $conversionResult = $amount * $exchangeRate;
    } else {
        $conversionResult = "Error: Could not retrieve exchange rate.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currency Converter</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <h1>Currency Converter</h1>

    <form action="index.php" method="POST">
        <label for="amount">Amount:</label>
        <input type="number" name="amount" id="amount" required>
        
        <label for="from_currency">From Currency:</label>
        <select name="from_currency" id="from_currency">
            <option value="USD">USD</option>
            <option value="EUR">EUR</option>
            <option value="GBP">GBP</option>
            <option value="JPY">JPY</option>
            <!-- Add more currencies as needed -->
        </select>

        <label for="to_currency">To Currency:</label>
        <select name="to_currency" id="to_currency">
            <option value="USD">USD</option>
            <option value="EUR">EUR</option>
            <option value="GBP">GBP</option>
            <option value="JPY">JPY</option>
            <!-- Add more currencies as needed -->
        </select>

        <button type="submit">Convert</button>
    </form>

    <?php if ($conversionResult !== null): ?>
        <h2>Conversion Result</h2>
        <p><?php echo "$amount $from_currency = " . round($conversionResult, 2) . " $to_currency"; ?></p>
    <?php endif; ?>

</body>
</html>
