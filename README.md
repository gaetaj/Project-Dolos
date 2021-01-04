<h1>Project Dolos</h1>	

<h2>Purpose</h2>
<p>To be able to identify sources of leaks of distributed executable files. The project in it's current state is very simple, but powerful. The idea of this is to make use of a concept called steganography. We hide a unique hash inside a binary and disguise it as normal code. When you do the insertion we return a hash. The imagined scenario would be a download that requires a user login, you could hide the hash in this binary, save the hash into your database and associate it with the user. Lets say this is a licensed product, the user bypasses the licensing system and distributes a tampered binary. Then if you discover this tampered binary, you can simply retrieve the hash and match it against your database of users with their associated hashes. The leaker would then be identified.

<h2>CMD Tool Usage</h2>
<code>usage: dolos.py [-h] [--retrieve] [--insert] binary_path</code>
