from preprocessing import preprocess_review  

# Probar la función con un ejemplo
if __name__ == "__main__":
    test_review = "This is an amazing product! I would definitely recommend it. runnin                      g#345"
    processed_review = preprocess_review(test_review)
    print("Review original:", test_review)
    print("Review procesado:", processed_review)
