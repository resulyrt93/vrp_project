import React from 'react';
import {Button, Form, InputNumber, Space} from "antd";
import {MinusCircleOutlined, PlusOutlined} from "@ant-design/icons";

const JobList = ({onValuesChange}) => {
  return (
    <div>
      <Form onValuesChange={onValuesChange} autoComplete="off">
        <Form.List name="jobs">
          {(fields, {add, remove}) => (
            <>
              {fields.map(({key, name, fieldKey, ...restField}) => (
                <Space key={key} style={{display: 'flex', marginBottom: 8}} align="baseline">
                  <Form.Item
                    {...restField}
                    name={[name, 'delivery']}
                    fieldKey={[fieldKey, 'delivery']}
                    rules={[{required: true, message: 'Missing Delivery Quantity'}]}
                  >
                    <InputNumber placeholder="Delivery Quantity"/>
                  </Form.Item>
                  <Form.Item
                    {...restField}
                    name={[name, 'target']}
                    fieldKey={[fieldKey, 'target']}
                    rules={[{required: true, message: 'Missing Target Index'}]}
                  >
                    <InputNumber placeholder="Target Index"/>
                  </Form.Item>
                  <Form.Item
                    {...restField}
                    name={[name, 'service']}
                    fieldKey={[fieldKey, 'service']}
                  >
                    <InputNumber placeholder="Service Duration"/>
                  </Form.Item>
                  <MinusCircleOutlined onClick={() => remove(name)}/>
                </Space>
              ))}
              <Form.Item>
                <Button type="dashed" onClick={() => add()} block icon={<PlusOutlined/>}>
                  Add Job
                </Button>
              </Form.Item>
            </>
          )}
        </Form.List>
      </Form>
    </div>
  );
};

export default JobList;