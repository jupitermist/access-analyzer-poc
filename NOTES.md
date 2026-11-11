# Notes

This PoC explores an AI-assisted approach to anomaly detection in access logs. The evaluation dataset is synthetic, built around common misuse patterns such as self-restored privileges and permissions left after a transfer. In practice, misuse rarely shows up as failed logins; it looks like routine work by an account that already has access.

During implementation, it became clear that evaluating the detection capability itself depends heavily on the design of the evaluation dataset. In this PoC, the influence of the dataset design on the detection results could not be sufficiently isolated, making it difficult to evaluate the detection logic independently.

Rather than continuing to expand the detection logic, I treated dataset design as a separate challenge and refined this PoC from an operational perspective by implementing input validation, security measures, traceability, and audit-ready reporting.

This marks a reasonable stopping point for the current scope.
