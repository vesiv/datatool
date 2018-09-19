import pandas as pd
import glob
import sys, os
import numpy as np


def split_phones(df, phones): ## From Clean.py

    # Split Phones from one column to four

    df['Mobile'] = df['Phone Numbers'].str.extract('(...-...-....)\(M\)',expand=True)
    df['Mobile 2'] = df['Phone Numbers'].str.extract('...-...-....\(M\).*?(...-...-....)\(M\)',expand=True)
    df['Mobile 3'] = df['Phone Numbers'].str.extract('...-...-....\(M\).*?...-...-....\(M\).*?(...-...-....)\(M\)',expand=True)
    df['Home'] = df['Phone Numbers'].str.extract('(...-...-....)\(H\)',expand=True)
    df['Mobile'] = df['Phone Numbers'].str.extract('(...-...-....)\(C\)',expand=True)
    df['Mobile 2'] = df['Phone Numbers'].str.extract('...-...-....\(C\).*?(...-...-....)\(C\)',expand=True)
    df['Mobile 3'] = df['Phone Numbers'].str.extract('...-...-....\(C\).*?...-...-....\(C\).*?(...-...-....)\(C\)',expand=True)
    df = df.drop('Phone Numbers', 1)

def split_emails(df, emails): ## From Clean.py

    # Split Emails from one column to three

    df['Email'] = df['Emails'].str.extract('(.*?@.*?\....),?',expand=True)
    df['Email 2'] = df['Emails'].str.extract('.*@.*\....,\s(.*@.*\....)',expand=True)
    df['Email 3'] = df['Emails'].str.extract('.*@.*\....,\s.*@.*\....,\s(.*@.*\....)',expand=True)

def KicksiteMash(path_to_files=os.getcwd(), key='Id', **kwargs):


    path = path_to_files + '/*.csv'
    files = glob.glob(path)

    main = pd.DataFrame()

    for i in files:
        if "Active" in i:
            active = pd.read_csv(i, index_col=None, dtype=object)

        if "Frozen" in i:
            frozen = pd.read_csv(i, index_col=None, dtype=object)


        if "recurring" in i:
            billing = pd.read_csv(i, index_col=None, dtype=object)

        if "Prospect" in i:
            prospects = pd.read_csv(i, index_col=None, dtype=object)

        if "families" in i:
            fam  = pd.read_csv(i, index_col=None, dtype=object, names=['Family', 'Members', 'Created', 'Edit'])

        if "Inactive" in i:
            inactive  = pd.read_csv(i, index_col=None, dtype=object)

    # Rename for merge

    #con.rename(columns={'Inquiry Date': 'Date Added'}, inplace=True)
    #ranks.rename(columns={'Person': 'Full Name'}, inplace=True)

    # Drop columns we can't use

    active.drop(['Age', 'Send SMS', 'SMS Phone Carrier', 'Inactivated on', 'Full Address', 'Converted to student on'], axis=1, inplace=True, errors='ignore')

    inactive.drop(['Age', 'Send SMS', 'SMS Phone Carrier', 'Full Address','Inactivated on', 'Converted to student on'], axis=1, inplace=True, errors='ignore')

    prospects.drop(['Age', 'Send SMS', 'SMS Phone Carrier', 'Follow-up Reminder', 'Full Address'], axis=1, inplace=True, errors='ignore')

    frozen.drop(['Age', 'Send SMS', 'SMS Phone Carrier', 'Full Address'], axis=1, inplace=True, errors='ignore')

    # Clean up

    ## Prospects ##

    contactTypes = {'trial': 'T', "archived": "FP"}
    prospects['Prospect Status'] = prospects['Prospect Status'].map(contactTypes)
    prospects.rename(columns={'Prospect Status': 'Contact Type', 'Prospect Source': 'Source', 'Phone': 'Mobile'}, inplace=True)

    ## Frozen ##

    frozen.drop(['Frozen','Frozen on','Freeze Until'], axis=1, inplace=True)
    active = active.append(frozen, sort=False)
    # append frozen to active -- they are treated as regular students

    ## Active ##

    contactTypes = {'Yes': 'S', "No": "F"}
    active['Active'] = active['Active'].map(contactTypes)
    active.rename(columns={'Active': 'Contact Type', 'Student Source': 'Source'}, inplace=True)

    ## Inactive ##

    inactive['Active'].replace({'No': 'F', 'Yes':"A"}, inplace=True)
    inactive.rename(columns={'Active': 'Contact Type','Student Source': 'Source'}, inplace=True)

    # All Sheets
    sheets = [active, prospects, inactive]
    for sheet in sheets:
        sheet['Gender'].replace({'Female': 'F', 'Male':"M"}, inplace=True)
        if 'Guardians' in sheet.columns.values:
            sheet['Guardians'], sheet['Guardian 2'] = sheet['Guardians'].str.split(',', 1).str
            split_phones(sheet, 'Phone Numbers')
            split_emails(sheet, 'Emails')
            sheet.drop(['Emails', 'Phone Numbers'], axis=1, inplace=True)
            phone_cols = ['Mobile', 'Mobile 2', 'Mobile 3', 'Home', 'SMS Phone']
            for phone in phone_cols:
                sheet[phone] = sheet[phone].replace(r'[^0-9]','', regex=True)


    ## Families ##

    fam.drop(['Edit', 'Created'], inplace=True, axis=1)
    index = len(fam.index.values)
    for rowIndex, row in fam.iterrows():
        if '\n' in row['Members']:
            members = row['Members'].split('\n')
            for member in members:
                index += 1
                fam.loc[index] = [row['Family'], member]
        fam.drop(rowIndex, inplace=True)

    fam['Members'] = fam['Members'].str.extract('(.*)\s\d+',expand=True)

    ## Memberships ##

    # split famliy memberships into individuals based on family file

    fam_billing = billing[pd.isnull(billing['Billable first name'])]
    billing = billing[pd.notnull(billing['Billable first name'])]
    billing['Members'] = billing['Billable first name'] + ' ' + billing['Billable last name']
    fam_billing.rename(columns={'Billable last name': 'Family'}, inplace=True)
    fam_billing = fam_billing.merge(fam, on='Family')
    billing = billing.append(fam_billing, sort=False)

    # drop excess columns

    billing.drop(['Inactivated Date','Auto Inactivated', 'Consecutive Declines',
        'Last Declined Date', 'Days until next charge', 'Billable first name',
        'Billable last name', 'Family'], axis=1, inplace=True)

    # takes active membership
    billing = billing.sort_values('Status').drop_duplicates(subset=['Members'],keep='first')


    ## Merge files ##

    complete = pd.DataFrame()
    for i in sheets:
        complete = complete.append(i, sort=False)

    complete['Members'] = complete['First Name'] + (" " + complete['Last Name'] if len(complete['Last Name']) != 0 else "")
    complete = complete.merge(billing, on='Members', how='left')

    ## Output files ##

    try:
        os.mkdir('clean')
    except Exception:
        pass

    active.name = 'Active'
    billing.name = 'Memberships'
    fam.name = 'Families'
    inactive.name = 'Inactive'
    frozen.name = 'Frozen'
    prospects.name = 'Prospects'
    complete.name = 'Complete_File'

    for i in [*sheets, billing, fam, complete]:

        i.to_csv('clean/' + i.name + '.csv', quoting=1, index=False)