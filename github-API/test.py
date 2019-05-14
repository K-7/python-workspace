from github3 import login


gh = login('kenith.777@gmail.com', password='prana247908')

sigmavirus24 = gh.me()
print "================="
print(sigmavirus24.name)
print(sigmavirus24.login)
print(sigmavirus24.followers_count)
organization = gh.organization('my-organization-name')
for team in organization.teams():
    if team.name == 'my-team-name':
        break
else:
    raise SystemExit('Could not find team named "my-team-name"')

for member in team.members():
     print('{}\t{}'.format(member.login, member.name))


# from github import Github
# g = Github('kenith.777@gmail.com', 'prana247908')

# org = g.get_organization(GH_ORG) //GH_ORG is organization name
# teams = org.get_teams()
# for t in teams:
#     if t.name == GH_TEAM:
#         for m in t.get_members():
#             print(m.login)