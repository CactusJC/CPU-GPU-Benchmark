from benchmark.database import CPU_BENCHMARKS

def generate_report(score, db):
  """
  Generates a report comparing the benchmark score against a database of scores.
  """
  # Create a copy to avoid modifying the original list
  db_copy = db.copy()
  db_copy.append({"name": "Your System", "score": score})

  # Sort the database by score in descending order
  db_copy.sort(key=lambda x: x["score"], reverse=True)

  print("Benchmark Comparison Report:")
  print("(Note: Score is a relative value for comparison within this tool only)")
  print("-" * 40)
  for i, entry in enumerate(db):
    # Highlight the user's system in the report
    if entry["name"] == "Your System":
      print(f"-> {i+1}. {entry['name']}: {entry['score']}")
    else:
      print(f"   {i+1}. {entry['name']}: {entry['score']}")
  print("-" * 40)

def calculate_score(time):
  """
  Converts the benchmark time into a score.
  The lower the time, the higher the score.
  This is a simple linear inversion formula for relative comparison.
  """
  return int(100000 / time)

if __name__ == '__main__':
  # Example usage
  my_score = calculate_score(38.338)
  generate_report(my_score, CPU_BENCHMARKS)
