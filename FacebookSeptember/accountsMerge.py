class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        accounts_map = {}
        for count,acc in enumerate(accounts):
            for index,details in enumerate(acc):
                if index > 0:
                    if details in accounts_map.keys():
                        for i in range(1,len(acc)):
                            if details != acc[i]:
                                accounts_map[details].append(acc[i])
                    else:
                        accounts_map[details] = [count]
                        for i in range(1,len(acc)):
                            if details != acc[i]:
                                accounts_map[details].append(acc[i])

        visited_emails = []
        current_visiting_emails = []
        def visit_email(email):
            if len(accounts_map[email])>1:
                for ind,to_visit_email in enumerate(accounts_map[email]):
                        if ind != 0 and to_visit_email not in visited_emails:
                            current_visiting_emails.append(to_visit_email)
                            visited_emails.append(to_visit_email)
                            visit_email(to_visit_email)

        rez =[]
        for email in accounts_map.keys():
            if email not in visited_emails:
                current_visiting_emails = [accounts_map[email][0],email]
                visited_emails.append(email)
                visit_email(email)
                rez.append([accounts[accounts_map[email][0]][0]] + sorted(current_visiting_emails[1:]))



        return rez
        
s = Solution()
print(s.accountsMerge(accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnmuie@mail.com","john_newyork@mail.com"] ,["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))