class InstagramAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password          # private
        self.__private_reels = []            # private
        self.__archived_reels = []           # private

    # Add private reel
    def add_private_reel(self, reel):
        self.__private_reels.append(reel)

    # Add archived reel
    def add_archived_reel(self, reel):
        self.__archived_reels.append(reel)

    # Display private reels (follower check)
    def show_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:", self.__private_reels)
        else:
            print("You are not a follower. Access denied.")

    # Display archived reels (password check)
    def show_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:", self.__archived_reels)
        else:
            print("Wrong password. Cannot access archived reels.")

    # Setter to update password
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully.")
        else:
            print("Old password is incorrect.")


# ---------------- OBJECT CREATION ----------------

account = InstagramAccount("john_doe", "1234")

# Add private reels
account.add_private_reel("Gym Reel")
account.add_private_reel("Travel Reel")

# Add archived reels
account.add_archived_reel("Old Birthday Reel")
account.add_archived_reel("College Memories Reel")

print("\n--- Private Reels Access ---")
account.show_private_reels(is_follower=True)
account.show_private_reels(is_follower=False)

print("\n--- Archived Reels Access ---")
account.show_archived_reels("1234")   # correct password
account.show_archived_reels("0000")   # wrong password

print("\n--- Update Password ---")
account.set_password("1234", "5678")

print("\n--- Archived Reels After Password Update ---")
account.show_archived_reels("5678")   # new password
account.show_archived_reels("1234")   # old password