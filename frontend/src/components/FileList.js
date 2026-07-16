import React from "react";
import API from "../api";

function FileList({ files, refreshFiles }) {

  const deleteFile = async (filename) => {

    if (!window.confirm("Delete this file?")) return;

    await API.delete(`/s3/files/${filename}`);

    refreshFiles();
  };

  return (
    <div className="card">

      <h3>Uploaded Files</h3>

      <table>

        <thead>

          <tr>
            <th>Name</th>
            <th>Size</th>
            <th>Action</th>
          </tr>

        </thead>

        <tbody>

          {files.map((file) => (

            <tr key={file.name}>

              <td>{file.name}</td>

              <td>{file.size} Bytes</td>

              <td>

                <button
                  onClick={() => deleteFile(file.name)}
                >
                  Delete
                </button>

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default FileList;
