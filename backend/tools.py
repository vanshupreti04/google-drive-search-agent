from drive_service import search_drive_files


class DriveSearchTool:
    name = "drive_search_tool"
    description = "Search files in Google Drive using Google Drive API q parameter."

    def run(self, q: str):
        return search_drive_files(q)