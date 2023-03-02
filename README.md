# Fingerprint Based Biometric Encryption

## REQUIREMENTS
Fernet<br>
base64 <br>
hashlib<br>

## ARCHITECTURE ILLUSTRATIONS
<b> Tier 1 </b> Data Collection <br>
<b> Tier 2 </b> Encryption and Decryption <br>
<b> Tier 3 </b> Data Storage and Retrieval <br><br>
First, we will get to know how we collect user data and what we do with their biometric data and how the collected data will be stored in the database.After getting the biometric data input as an image of the user’s fingerprint. We will come up with a method to create data from the fingerprint by measuring various fingerprint Minutiaes and characteristics. <br>

### ARCHITECTURE ILLUSTRATIONS - FLOW CONTROL 1
<b> Generating Data (Table of Features) from Fingerprint Image </b>
![image](https://user-images.githubusercontent.com/68748665/222432194-aa91f94d-5cbf-4d7d-b809-b2214c081b28.png) <br><br>
Once we generate data from the user's fingerprint, we will generate a unique Unicode String out of it by following standard Unicode string generation algorithms. <br>

<b> Generating Unicode String from the Generated Fingerprint Data </b>
![image](https://user-images.githubusercontent.com/68748665/222432539-4add129e-fce2-469f-a9dd-a11357e28fdd.png)<br><br>
Once a unique key is generated for the user, we will use the key and a custom encryption algorithm that takes the key as an input and encrypts the user data and in addition, we will also be encrypting a known data named dummy data using the encryption algorithm and the user's unique key. <br>

<b>Generating Encrypted User Data and Dummy Data with Hash Algorithm Along with the Unicode </b>
![image](https://user-images.githubusercontent.com/68748665/222432927-876b4289-2e67-4cfb-b505-7eb5ec7c0e19.png)<br><br>
Once both the user data and the known dummy data is encrypted, we will be storing the User_ID, User_Name, Encrypted_Dummy_Data and Encrypted_User_Data in our database (Fig 3.6). Notice that we are not storing the User’s biometric data or the unique key generated out of it thereby eliminating all possible ways for the company itself to decrypt the confidential information. <br>

![image](https://user-images.githubusercontent.com/68748665/222433579-a1f8da41-6e18-41f7-9747-88878367cae4.png)<br><br>

### ARCHITECTURE ILLUSTRATIONS - FLOW CONTROL 2
Once the data is successfully collected and stored in the database, now we will look into the authentication and data retrieval procedure. We will again need to get the biometric information of the user in the form of an image of their fingerprint and then we will again generate data out of it.<br>
![image](https://user-images.githubusercontent.com/68748665/222433850-fa421eea-a69e-4ea5-a2ae-ea18eb3d6e77.png)<br><br>

Then from the data collected from the user’s fingerprint we will be using the same Unicode Key Generation techniques to create a unique key for the user (Fig 3.8). We also made sure that our Unicode key generation algorithm will always generate the same Unicode key when the same fingerprint data is given as input again and again. <br>

![image](https://user-images.githubusercontent.com/68748665/222433957-2218459c-fe64-4009-b310-f6b3a5266aa2.png)<br><br>

Now, to authenticate the user we will be using the same encryption algorithm and the key generated to encrypt the dummy data (already known data) and match it against the already encrypted dummy data. Only if both the encrypted dummy data match, we can authenticate the user and use the same key to decrypt the encrypted user data and showcase it to the user. (Fig 5.9)<br>

![image](https://user-images.githubusercontent.com/68748665/222434083-85f50825-1fad-42dd-ad44-7652bac84eab.png)<br><br>

## DISCUSSIONS
### Passkeys in Apple
According to Apple, Passkeys are a replacement for passwords that are designed to provide a more convenient, more secure, password-less sign-in experience on websites and apps. Passkeys are a standard-based technology that, unlike passwords, are resistant to phishing, always strong and designed so that there are no shared secrets. They simplify the account registration process for apps and websites, are easy to use and work across all your Apple devices, and even non-Apple devices within close physical proximity.

### How is it being used in Google?
On Chrome on Android, passkeys are stored in the Google Password Manager, which synchronizes passkeys between the user's Android devices that are signed into the same Google account. Users are not restricted to using the passkeys only on the device where they are stored. Passkeys stored on phones can be used when logging into a laptop, even if the passkey is not synchronized to the laptop, as long as the phone is near the laptop and the user approves the sign-in on the phone. As passkeys are built on FIDO standards, all browsers can adopt them.

## CONCLUSION
Thus we came up with a working solution to meet the demand of our problem statement of storing and retrieving confidential information using biometric encryption where no one except the user themselves is capable of retrieving and decrypting the confidential information.

