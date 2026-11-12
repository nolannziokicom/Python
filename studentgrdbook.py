print("Student grade book")
grades={"name": "charles",
        "score": "90",

        "name":"amy",
        "score":"95",

        "name":"brian",
        "score": "85",

        "name":"daniel",
        "score":"90",

        "name":"Caleb",
        "score":"88"

        }
total=0
for name in grades:
    total=total+grades
    avg=total/len(grades)
    print("Average is",avg)

top_name=""
top_score=0






# ---------- PART 3: highest score ----------
# YOUR CODE HERE
# Make top_name = "" and top_score = 0.
# Loop over grades. If a score is higher than top_score,
# save that name in top_name and that score in top_score.
# Print the highest scorer and the score.

# ---------- PART 4: look up a student ----------
# YOUR CODE HERE
# Ask for a student name with input().
# Print the score with .get(). Use "Not found" if the name is not in grades.

