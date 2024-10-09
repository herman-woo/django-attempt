from model.Status import Status
from model.Submission import Submission

print("Hello")

newestSubmission = Submission(123,Status.SUBMISSION)


print(newestSubmission.policy_id,newestSubmission.status.value)