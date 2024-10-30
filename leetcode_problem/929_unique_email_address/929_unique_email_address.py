# https://leetcode.com/problems/unique-email-addresses/description/
# https://www.youtube.com/watch?v=TC_xLIWl7qY

def numUniqueEmails(emails):
    hashSet = set()

    for e in emails:
        local, domain = e.split("@")

        # remove string after "+" in domain
        local = local.split("+")[0]

        # remove "."
        local = local.replace(".", "")

        # add tuple to hashSet
        # if element is duplicated, set will not add it
        hashSet.add((local, domain))

    return len(hashSet)


lst = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
print(numUniqueEmails(lst))
