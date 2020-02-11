class Tree:
  def __init__(self, root_value):
    self.root = { 'value': root_value, 'left': None, 'right': None }

  def addChild(self, value):
    current_node = self.root
    while current_node is not None:
      if value < current_node.get('value'):
          if current_node.get('left') is None:
            current_node['left'] = {'value': value, 'left': None, 'right': None}
            break
          else:
            current_node = current_node.get('left')
      else:
        if current_node.get('right') is None:
            current_node['right'] = {'value': value, 'left': None, 'right': None}
            break
        else:
          current_node = current_node.get('right')

  def traverse(self, str, root, expression):
    if root is None:
      return str

    str += f"{root.get('value')}"
    expression(root.get('value'))

    str += self.traverse('', root.get('left'), expression)
    str += self.traverse('', root.get('right'), expression)

    return str
  
  def get_lower(self, node):
    current_node = node
    while current_node['left'] is not None:
      current_node = current_node['left']

    return current_node

  def delete(self, value):
    if self.root is not None:
      current_node = self.root

      while current_node is not None:
        if current_node['left'] is not None and current_node['left'].get('value') == value:
          temp_node = current_node.get('left')
          if temp_node['left'] is None and temp_node['right'] is None:
            current_node['left'] = None
          elif temp_node['left'] is not None and temp_node['right'] is not None:
            node = self.get_lower(temp_node['right'])
            save_current_node_child = temp_node['rigth']
            current_node['left'] = node
            if node['right'] is not None:
              node['right'] = save_current_node_child
          elif temp_node['left'] is not None or temp_node['right'] is not None:
            child = 'left' if temp_node['left'] is not None else 'right'
            node = temp_node.get(child)
            current_node.get('left')[child] = node
          break

        if current_node['right'] is not None and current_node['right'].get('value') == value:
          current_node['right'] = None
          break
