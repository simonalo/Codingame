
let [width, height] = readline().split(' ').map(n => +n)
let grid = []
while (height--) {
  grid.push(readline().split(''))
}

/**
 * Deeply clone an array or an object
 * @param {Any} obj - object to be cloned
 * @return {Any} a clone of this object
 */
let clone = (obj) => {
  if (Array.isArray(obj)) {
    return obj.map(n => clone(n))
  } else if (obj instanceof Object) {
    let res = {}
    for (let i in obj) {
      res[i] = clone(obj[i])
    }
    return res
  }
  return obj
}

/**
 * Display grid for debugging
 * @param {Array<Array<String>>} grid to be displayed
 */
let debugGrid = (grid) => {
  printErr(' ', grid[0].map((n, i) => i).join(' '))
  grid.forEach((row, i) => printErr(i, row.join(' ')))
}

/**
 * Count remaining nodes on grid
 * @param {Array<Array<String>>} grid containing nodes and walls
 */
let countNodes = (grid) => grid.reduce(((s, row) => s + row.reduce((s, c) => s + (c === '@'/* || !isNaN(c)*/ ? 1 : 0), 0)), 0)

/**
 * Apply a bomb explosition into the grid, taking walls into account
 * Three working mode:
 * - immediate removes immediately nodes
 * - non immediate place countdown on nodes that are in the bomb range
 * - simulate does not modify anything, and just count how many nodes are affected
 * @param {Array<Array<String>>} grid containing nodes and walls
 * @param {Number} x - abscissa of the bomb
 * @param {Number} y - ordinate of the bomb
 * @param {Boolean=true} immediate - toggle immediate mode
 * @param {Boolean=false} simulate - toggle simulation mode
 * @return {Number} count of nodes affected by bomb blow
 */
let applyExplosion = (grid, x, y, immediate=true, simulate=false) => {
  grid[y][x] = '.'
  let count = applyBlow(grid, x + 1, y, true, 2, immediate, simulate)
  count += applyBlow(grid, x - 1, y, true, -2, immediate, simulate)
  count += applyBlow(grid, x, y + 1, false, 2, immediate, simulate)
  count += applyBlow(grid, x, y - 1, false, -2, immediate, simulate)
  return count
}

/**
 * Apply an explosiion blow on a row/column, in one direction
 * Three working mode:
 * - immediate removes immediately nodes
 * - non immediate place countdown on nodes that are in the bomb range
 * - simulate does not modify anything, and just count how many nodes are affected
 * @param {Array<Array<String>>} grid containing nodes and walls
 * @param {Number} x - abscissa of the bomb
 * @param {Number} y - ordinate of the bomb
 * @param {Boolean} horiz - true for a row, false for a column
 * @param {Number} until - number of cell blowed on the row/column.
 * Negative means left (for rows) or top (for columns), positive is right/bottom.
 * @param {Boolean=true} immediate - toggle immediate mode
 * @param {Boolean=false} simulate - toggle simulation mode
 * @return {Number} count of nodes affected by bomb blow on the row/column
 */
let applyBlow = (grid, x, y, horiz, until, immediate, simulate) => {
  let count = 0
  let stopped = until === 0
  if (grid[y] && x < grid[y].length) {
    if (grid[y][x] === '#') {
      // meet passive node
      stopped = true
    } else if (grid[y][x] === '@') {
      count++
      if (!simulate) {
        grid[y][x] = immediate ? '.' : 2
      }
    }
  } else {
    stopped = true
  }
  if (!stopped) {
    count += applyBlow(grid, x + (horiz ? until > 0 ? 1 : -1 : 0),
      y + (!horiz ? until > 0 ? 1 : -1 : 0), horiz,
      until + (until > 0 ? -1 : 1), immediate, simulate)
  }
  return count
}

/**
 * Decrement countdown for future exploded nodes
 * @param {Array<Array<String>>} grid containing nodes and walls
 */
let purgeGrid = (grid) => {
  grid.forEach((row, y) => row.forEach((cell, x) =>
    row[x] = cell === 2 || cell === 1 ? cell-1 : cell === 0 ? '.' : cell
  ))
}

/**
 * Simulate all game to return a winning sequence of bomb placement
 * Backtrack implementation.
 * Game is won when all nodes are blowed, and bombs are not depleted
 *
 * @param {Array<Array<String>>} unmodified grid containing nodes and walls
 * @param {Number} bombs - number of remaining bombs
 * @param {Array<Object> = []} seq - for private usage only, array of orders
 * @return {Array<Object>} winning sequence of orders, null if game not winnable.
 */
let simulate = (grid, bombs, seq = []) => {
  let remains = countNodes(grid)
  if (remains === 0) {
    // no more nodes to blow
    return seq
  }
  if (bombs === 0) {
    // no more bombs
    return null
  }
  // compute possible bomb locations
  let possibles = []
  grid.forEach((row, y) =>
    row.map((cell, x) => {
      let count = cell === '.' ? applyExplosion(grid, x, y, true, true) : 0
      if (count === remains || count > 1) {
        possibles.push({c: count, x: x, y: y})
      }
    })
  )
  // order them by number of destroyed nodes
  possibles.sort((a, b) => b.c - a.c)

  let idx = seq.length
  for (let possible of possibles) {
    seq.push(possible)
    let newGrid = clone(grid)
    applyExplosion(newGrid, possible.x, possible.y)

    let solution = simulate(newGrid, bombs-1, seq)
    if (solution) {
      // complete solution found !
      return seq
    }
    // backtrack possibility
    seq.splice(idx, seq.length)
  }
  // no solution found
  return null
}

let seq = null
// game loop
while (true) {
  let [rounds, bombs] = readline().split(' ').map(n => +n)
  purgeGrid(grid)

  if (!seq) {
    // compute winning order sequence, only when we got bomb numbers
    seq = simulate(grid, bombs)
  }

  let order = seq[0]
  if (!order || grid[order.y][order.x] !== '.') {
    print('wait')
  } else {
    seq.shift()
    applyExplosion(grid, order.x, order.y, false)
    print(order.x + ' ' + order.y)
  }
}
