import React from 'react';
import AceEditor from "react-ace";

import "ace-builds/src-noconflict/mode-json";
import "ace-builds/src-noconflict/theme-kuroir";
import {Form} from "antd";

const DrawerContent = () => {

  return (
    <div>
      <Form.Item name={'matrix'}
                 label={"Distance Matrix"}>
        <AceEditor
          mode="json"
          theme="kuroir"
          fontSize={16}
          showPrintMargin={true}
          showGutter={true}
          highlightActiveLine={true}
          setOptions={{
            enableBasicAutocompletion: true,
            enableLiveAutocompletion: true,
            enableSnippets: true,
            showLineNumbers: true,
            tabSize: 2,
          }}
        />
      </Form.Item>
    </div>
  );
};

export default DrawerContent;