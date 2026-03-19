# elite-auto-purchase
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Elite Auto Purchase | Custom Car Negotiations</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; }
    </style>
</head>
<body class="bg-slate-50 text-slate-900">

    <nav class="p-6 bg-white shadow-sm">
        <div class="max-w-5xl mx-auto flex justify-between items-center">
            <h1 class="text-2xl font-bold tracking-tight text-blue-900">ELITE AUTO PURCHASE</h1>
            <span class="text-sm font-medium text-slate-500 uppercase tracking-widest">Premium Concierge</span>
        </div>
    </nav>

    <header class="py-12 px-6 text-center max-w-3xl mx-auto">
        <h2 class="text-4xl font-extrabold mb-4">You Name the Price. <br><span class="text-blue-600">We Negotiate the Deal.</span></h2>
        <p class="text-slate-600 text-lg">Tell us exactly what you want to pay. We handle the dealerships, the paperwork, and the headaches.</p>
    </header>

    <section class="max-w-2xl mx-auto bg-white p-8 rounded-2xl shadow-xl mb-20 border border-slate-100">
        <form action="https://formspree.io/f/your-id-here" method="POST" class="space-y-6">
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                    <label class="block text-sm font-semibold mb-2">Vehicle Condition</label>
                    <select name="condition" class="w-full p-3 border rounded-lg bg-slate-50">
                        <option>New</option>
                        <option>Pre-Owned</option>
                    </select>
                </div>
                <div>
                    <label class="block text-sm font-semibold mb-2">Target Out-the-Door Price</label>
                    <input type="text" name="target_price" placeholder="$0.00" class="w-full p-3 border rounded-lg bg-slate-50" required>
                </div>
            </div>

            <div>
                <label class="block text-sm font-semibold mb-2">Vehicle Make & Model</label>
                <input type="text" name="vehicle_choice" placeholder="e.g. 2024 Ford Maverick XLT" class="w-full p-3 border rounded-lg bg-slate-50" required>
            </div>

            <div>
                <label class="block text-sm font-semibold mb-2">Warranty Preferences</label>
                <div class="space-y-2">
                    <label class="flex items-center text-sm text-slate-700">
                        <input type="checkbox" name="warranty_powertrain" class="mr-2"> Powertrain Protection
                    </label>
                    <label class="flex items-center text-sm text-slate-700">
                        <input type="checkbox" name="warranty_bumper" class="mr-2"> Full Bumper-to-Bumper
                    </label>
                    <label class="flex items-center text-sm text-slate-700">
                        <input type="checkbox" name="no_warranty" class="mr-2"> No Warranty (As-Is)
                    </label>
                </div>
            </div>

            <div>
                <label class="block text-sm font-semibold mb-2">How would you like to finish?</label>
                <select name="delivery_method" class="w-full p-3 border rounded-lg bg-slate-50">
                    <option>Home Delivery (VIP Service)</option>
                    <option>In-Person at Dealership</option>
                </select>
            </div>

            <hr class="border-slate-100">

            <div>
                <label class="block text-sm font-semibold mb-2">Your Contact Information</label>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <input type="text" name="name" placeholder="Full Name" class="w-full p-3 border rounded-lg bg-slate-50" required>
                    <input type="email" name="_replyto" placeholder="Email Address" class="w-full p-3 border rounded-lg bg-slate-50" required>
                </div>
            </div>

            <button type="submit" class="w-full bg-blue-900 text-white font-bold py-4 rounded-lg hover:bg-blue-800 transition shadow-lg uppercase tracking-wider">
                Begin My Negotiation
            </button>
        </form>
    </section>

    <footer class="text-center py-10 text-slate-400 text-sm">
        &copy; 2026 Elite Auto Purchase. All Rights Reserved.
    </footer>

</body>
</html>
