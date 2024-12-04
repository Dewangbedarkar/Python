# # # #!/usr/bin/env python3
# # # import sys
# # #
# # # # Read each line from standard input
# # # for line in sys.stdin:
# # #     line = line.strip()  # Remove leading and trailing whitespace
# # #
# # #     # Split the line into parts (ID, Value)
# # #     parts = line.split(',')
# # #
# # #     # Ensure the line has exactly 2 fields (ID and associated value)
# # #     if len(parts) == 2:
# # #         key, value = parts[0].strip(), parts[1].strip()
# # #
# # #         # Emit the key and tagged value (U: for user, P: for purchase)
# # #         if key.isdigit():  # Validate that the key is numeric
# # #             if value.isalpha():  # Alphabetic values belong to Users.csv
# # #                 print(f"{key}\tU:{value}")
# # #             else:  # Non-alphabetic values belong to Purchases.csv
# # #                 print(f"{key}\tP:{value}")
# #
# #
# # # !/usr/bin/env python3
# # import sys
# #
# # for line in sys.stdin:
# #     # Remove whitespace and split by commas
# #     line = line.strip()
# #     parts = line.split(",")
# #
# #     if len(parts) == 2:  # Ensure the line has exactly two fields
# #         key, value = parts
# #         # Tag the line based on file type
# #         if value.isalpha():  # Assuming names in Users.csv are alphabetic
# #             source = "user"
# #         else:  # Assuming purchases in Purchases.csv are non-alphabetic
# #             source = "purchase"
# #
# #         # Emit key-value pair
# #         print(f"{key}\t{source}:{value}")
#
#
# #!/usr/bin/env python3
# import sys
#
# for line in sys.stdin:
#     # Remove whitespace and split the line
#     line = line.strip()
#     parts = line.split("\t")
#
#     if len(parts) == 2:  # Ensure the line has exactly two tab-separated fields
#         key, value = parts
#         if value.startswith("user:name:") or value.startswith("user:item:"):
#             print(value)  # Emit the value directly without the key
#
