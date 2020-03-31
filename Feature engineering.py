
participants['Italian'] = 0
participants.loc[participants.Country == 'Italia', 'Italian'] = 1

participants.Date_of_birth = pd.to_datetime(participants.Date_of_birth)
participants.Date_of_election = pd.to_datetime(participants.Date_of_election)
participants


participants['Rank'] = participants.Title.apply(lambda x: 'CP' if x.split()[1] == 'presbitero' else 'CB' if x.split()[1] == 'vescovo' else 'CD')


participants['Emeritus'] = participants.Title2.apply(lambda x: 1 if x.split()[1] == 'emerito' else 0)


participants['Office'] = participants.Title2.apply(lambda x: 'Archbishop' if (x.split()[0] == 'Arcivescovo' or x.split()[0] == 'Vescovo' or x.split()[0] == 'Patriarca')else 'Prefect' if x.split()[0] == 'Prefetto' else 'Other_curia')


participants['Age_at_conclave'] = [relativedelta(a, b).years for a, b in zip(participants['Date'], participants['Date_of_birth'])]


participants['Card_seniority'] = [12 - relativedelta(a, b).months + relativedelta(a, b).years*12 for a, b in zip(participants['Date'], participants['Date_of_election'])]


participants1 = participants


participants1 = participants1.drop(['Country', 'Title', 'Title2', 'Date_of_birth', 'Date_of_election', 'Date'], 1)


participants1 = pd.concat([participants1.drop('Office', axis=1), pd.get_dummies(participants1['Office'])], axis=1)
participants1 = pd.concat([participants1.drop('Rank', axis=1), pd.get_dummies(participants1['Rank'])], axis=1)
participants1



