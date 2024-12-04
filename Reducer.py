# # #!/usr/bin/env python3
# # import sys
# #
# # # Initialize variables
# # current_key = None
# # user_name = None
# # purchases = []
# #
# # def emit_result(key, name, items):
# #     """Function to emit the join result."""
# #     if name and items:
# #         for item in items:
# #             print(f"{key}\t{name}\t{item}")
# #
# # # Process each line from standard input
# # for line in sys.stdin:
# #     line = line.strip()  # Remove leading and trailing whitespace
# #
# #     try:
# #         # Split the line into key and value
# #         key, value = line.split('\t', 1)
# #
# #         # Split value into type (U/P) and actual data
# #         value_type, data = value.split(':', 1)
# #     except ValueError:
# #         continue  # Skip lines with invalid format
# #
# #     if key != current_key:
# #         # Emit results for the previous key
# #         if current_key:
# #             emit_result(current_key, user_name, purchases)
# #
# #         # Reset variables for the new key
# #         current_key = key
# #         user_name = None
# #         purchases = []
# #
# #     # Process the value based on its type
# #     if value_type == 'U':  # User data
# #         user_name = data
# #     elif value_type == 'P':  # Purchase data
# #         purchases.append(data)
# #
# # # Emit the last key's results
# # if current_key:
# #     emit_result(current_key, user_name, purchases)
#
#
# # !/usr/bin/env python3
# import sys
#
# current_key = None
# user_name = None
# purchases = []
#
# for line in sys.stdin:
#     line = line.strip()
#     key, value = line.split("\t")
#     source, detail = value.split(":", 1)
#
#     if key != current_key:
#         # Output previous key if we have both user and purchase
#         if current_key and user_name:
#             for purchase in purchases:
#                 print(f"{current_key}\t{user_name}\t{purchase}")
#         # Reset for new key
#         current_key = key
#         user_name = None
#         purchases = []
#
#     # Collect data based on source
#     if source == "user":
#         user_name = detail
#     elif source == "purchase":
#         purchases.append(detail)
#
# # Emit the last key
# if current_key and user_name:
#     for purchase in purchases:
#         print(f"{current_key}\t{user_name}\t{purchase}")


# !/usr/bin/env python3
import sys

# Initialize variables
current_id = None
name = None
items = []

for line in sys.stdin:
    # Strip whitespace and split input
    line = line.strip()
    key, value = line.split("\t", 1)
    _, data_type, detail = value.split(":", 2)

    # If a new key is encountered
    if key != current_id:
        # Emit the result for the previous key
        if current_id and name:
            for item in items:
                print(f"{current_id}\t{name}\t{item}")
        # Reset for the new key
        current_id = key
        name = None
        items = []

    # Collect name or items based on data_type
    if data_type == "name":
        name = detail
    elif data_type == "item":
        items.append(detail)

# Emit the last key
if current_id and name:
    for item in items:
        print(f"{current_id}\t{name}\t{item}")

