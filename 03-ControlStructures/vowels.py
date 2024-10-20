###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
i = 0
# Count vowels in the text
while True :
        for char in text:
            if char in vowels:
              vowel_count += 1
        break
      
    
        
    
  
    


print(f"The number of vowels in the text is: {vowel_count}")
