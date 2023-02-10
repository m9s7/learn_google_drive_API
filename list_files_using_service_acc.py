def list_files_in_drive(service):
    fileList = {"spreadsheet": [], "excel": []}
    pageToken = ""
    while pageToken is not None:

        # Mogu da ubacim support za .xls ako ih imate
        # application/vnd.ms-excel
        res = service.files().list(
            q="(mimeType='application/vnd.google-apps.spreadsheet' or mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet') and trashed=false",
            fields="nextPageToken, files(id,name,mimeType)", pageSize=1000, pageToken=pageToken, corpora="allDrives",
            includeItemsFromAllDrives=True, supportsAllDrives=True).execute()

        for e in res.get("files", []):
            if e["mimeType"] == "application/vnd.google-apps.spreadsheet":
                del e["mimeType"]
                fileList["spreadsheet"].append(e)
            elif e["mimeType"] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                del e["mimeType"]
                fileList["excel"].append(e)
        pageToken = res.get("nextPageToken")

    print(fileList)
